import { Button } from '@/components/ui/button';
import { ThemeToggle } from '@/components/theme-toggle';

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center gap-8 p-8">
      <div className="flex flex-col items-center gap-4 text-center">
        <h1 className="text-4xl font-bold tracking-tight">
          Welcome to SlotReader
        </h1>
        <p className="text-muted-foreground text-lg">
          An adaptive reading web app for scheduling daily reading slots
        </p>
      </div>

      <div className="flex items-center gap-4">
        <ThemeToggle />
        <Button variant="default">Get Started</Button>
        <Button variant="secondary">Learn More</Button>
        <Button variant="outline">Documentation</Button>
      </div>
    </div>
  );
}
